class Colormap2D:
    """
    Baseclass for all size 2 iterables to RGBA mappings, based on
    matplotlib's Colormap class.
    Colormap2D instances are used to convert two scalars each from the
    interval ``[0, 1]`` to the RGBA color that the respective Colormap2D
    represents. For scaling of data into the ``[0, 1]`` interval see
    `matplotlib.colors.Normalize`.
    """

    def __init__(self, name, N=256):
        """
        Parameters
        ----------
        name : str
            The name of the colormap.
        N : int
            The number of rgb quantization levels.
        """
        self.name = name
        self.N = int(N)  # ensure that N is always int
        self._rgba_bad = (0.0, 0.0, 0.0, 0.0)  # If bad, don't paint anything.
        self._rgba_under = None
        self._rgba_over = None
        self._i_under = self.N
        self._i_over = self.N + 1
        self._i_bad = self.N + 2
        self._isinit = False
        #: When this colormap exists on a scalar mappable and colorbar_extend
        #: is not False, colorbar creation will pick up ``colorbar_extend`` as
        #: the default value for the ``extend`` keyword in the
        #: `matplotlib.colorbar.Colorbar` constructor.
        self.colorbar_extend = False

    def __call__(self, X, alpha=None, bytes=False):
        """
        Parameters
        ----------
        X : float or int, 2xM ndarray
            The data value(s) to convert to RGBA.
            For floats, X should be in the interval ``[0.0, 1.0]`` to
            return the RGBA values ``X*100`` percent along the Colormap line.
            For integers, X should be in the interval ``[0, Colormap.N)`` to
            return RGBA values *indexed* from the Colormap with index ``X``.
        alpha : float or array-like or None
            Alpha must be a scalar between 0 and 1, a sequence of such
            floats with shape matching X, or None.
        bytes : bool
            If False (default), the returned RGBA values will be floats in the
            interval ``[0, 1]`` otherwise they will be uint8s in the interval
            ``[0, 255]``.
        Returns
        -------
        Tuple of RGBA values if X is scalar, otherwise an array of
        RGBA values with a shape of ``X.shape[1] + (4, )``.
        """
        if not self._isinit:
            self._init()

        # Take the bad mask from a masked array, or in all other cases defer
        # np.isnan() to after we have converted to an array.
        mask_bad = X.mask if np.ma.is_masked(X) else None
        xa = np.array(X, copy=True)
        if mask_bad is None:
            mask_bad = np.isnan(xa)
        if not xa.dtype.isnative:
            xa = xa.byteswap().newbyteorder()  # Native byteorder is faster.
        if xa.dtype.kind == "f":
            with np.errstate(invalid="ignore"):
                xa *= self.N
                # Negative values are out of range, but astype(int) would
                # truncate them towards zero.
                xa[xa < 0] = -1
                # xa == 1 (== N after multiplication) is not out of range.
                xa[xa == self.N] = self.N - 1
                # Avoid converting large positive values to negative integers.
                np.clip(xa, -1, self.N, out=xa)
                xa = xa.astype(int)
        # Set the over-range indices before the under-range;
        # otherwise the under-range values get converted to over-range.
        xa[xa > self.N - 1] = self._i_over
        xa[xa < 0] = self._i_under
        xa[mask_bad] = self._i_bad

        lut = self._lut
        if bytes:
            lut = (lut * 255).astype(np.uint8)

        rgba = lut.take(xa, axis=0, mode='clip')

        if alpha is not None:
            alpha = np.clip(alpha, 0, 1)
            if bytes:
                alpha *= 255  # Will be cast to uint8 upon assignment.
            if alpha.shape not in [(), xa.shape]:
                raise ValueError(
                    f"alpha is array-like but its shape {alpha.shape} does "
                    f"not match that of X {xa.shape}")
            rgba[..., -1] = alpha

            # If the "bad" color is all zeros, then ignore alpha input.
            if (lut[-1] == 0).all() and np.any(mask_bad):
                if np.iterable(mask_bad) and mask_bad.shape == xa.shape:
                    rgba[mask_bad] = (0, 0, 0, 0)
                else:
                    rgba[..., :] = (0, 0, 0, 0)

        if not np.iterable(X):
            rgba = tuple(rgba)
        return rgba

    def __copy__(self):
        cls = self.__class__
        cmapobject = cls.__new__(cls)
        cmapobject.__dict__.update(self.__dict__)
        if self._isinit:
            cmapobject._lut = np.copy(self._lut)
        return cmapobject

    def __eq__(self, other):
        if (not isinstance(other, Colormap) or self.name != other.name or
                self.colorbar_extend != other.colorbar_extend):
            return False
        # To compare lookup tables the Colormaps have to be initialized
        if not self._isinit:
            self._init()
        if not other._isinit:
            other._init()
        return np.array_equal(self._lut, other._lut)

    def get_bad(self):
        """Get the color for masked values."""
        if not self._isinit:
            self._init()
        return np.array(self._lut[self._i_bad])

    def set_bad(self, color='k', alpha=None):
        """Set the color for masked values."""
        self._rgba_bad = to_rgba(color, alpha)
        if self._isinit:
            self._set_extremes()

    def get_under(self):
        """Get the color for low out-of-range values."""
        if not self._isinit:
            self._init()
        return np.array(self._lut[self._i_under])

    def set_under(self, color='k', alpha=None):
        """Set the color for low out-of-range values."""
        self._rgba_under = to_rgba(color, alpha)
        if self._isinit:
            self._set_extremes()

    def get_over(self):
        """Get the color for high out-of-range values."""
        if not self._isinit:
            self._init()
        return np.array(self._lut[self._i_over])

    def set_over(self, color='k', alpha=None):
        """Set the color for high out-of-range values."""
        self._rgba_over = to_rgba(color, alpha)
        if self._isinit:
            self._set_extremes()

    def set_extremes(self, *, bad=None, under=None, over=None):
        """
        Set the colors for masked (*bad*) values and, when ``norm.clip =
        False``, low (*under*) and high (*over*) out-of-range values.
        """
        if bad is not None:
            self.set_bad(bad)
        if under is not None:
            self.set_under(under)
        if over is not None:
            self.set_over(over)

    def with_extremes(self, *, bad=None, under=None, over=None):
        """
        Return a copy of the colormap, for which the colors for masked (*bad*)
        values and, when ``norm.clip = False``, low (*under*) and high (*over*)
        out-of-range values, have been set accordingly.
        """
        new_cm = self.copy()
        new_cm.set_extremes(bad=bad, under=under, over=over)
        return new_cm

    def _set_extremes(self):
        if self._rgba_under:
            self._lut[self._i_under] = self._rgba_under
        else:
            self._lut[self._i_under] = self._lut[0]
        if self._rgba_over:
            self._lut[self._i_over] = self._rgba_over
        else:
            self._lut[self._i_over] = self._lut[self.N - 1]
        self._lut[self._i_bad] = self._rgba_bad

    def _init(self):
        """Generate the lookup table, ``self._lut``."""
        raise NotImplementedError("Abstract class only")

    def is_gray(self):
        """Return whether the colormap is grayscale."""
        if not self._isinit:
            self._init()
        return (np.all(self._lut[:, 0] == self._lut[:, 1]) and
                np.all(self._lut[:, 0] == self._lut[:, 2]))

    def resampled(self, lutsize):
        """Return a new colormap with *lutsize* entries."""
        if hasattr(self, '_resample'):
            _api.warn_external(
                "The ability to resample a color map is now public API "
                f"However the class {type(self)} still only implements "
                "the previous private _resample method.  Please update "
                "your class."
            )
            return self._resample(lutsize)

        raise NotImplementedError()

    def reversed(self, name=None):
        """
        Return a reversed instance of the Colormap.
        .. note:: This function is not implemented for the base class.
        Parameters
        ----------
        name : str, optional
            The name for the reversed colormap. If None, the
            name is set to ``self.name + "_r"``.
        See Also
        --------
        LinearSegmentedColormap.reversed
        ListedColormap.reversed
        """
        raise NotImplementedError()

    def _repr_png_(self):
        """Generate a PNG representation of the Colormap."""
        X = np.tile(np.linspace(0, 1, _REPR_PNG_SIZE[0]),
                    (_REPR_PNG_SIZE[1], 1))
        pixels = self(X, bytes=True)
        png_bytes = io.BytesIO()
        title = self.name + ' colormap'
        author = f'Matplotlib v{mpl.__version__}, https://matplotlib.org'
        pnginfo = PngInfo()
        pnginfo.add_text('Title', title)
        pnginfo.add_text('Description', title)
        pnginfo.add_text('Author', author)
        pnginfo.add_text('Software', author)
        Image.fromarray(pixels).save(png_bytes, format='png', pnginfo=pnginfo)
        return png_bytes.getvalue()

    def _repr_html_(self):
        """Generate an HTML representation of the Colormap."""
        png_bytes = self._repr_png_()
        png_base64 = base64.b64encode(png_bytes).decode('ascii')
        def color_block(color):
            hex_color = to_hex(color, keep_alpha=True)
            return (f'<div title="{hex_color}" '
                    'style="display: inline-block; '
                    'width: 1em; height: 1em; '
                    'margin: 0; '
                    'vertical-align: middle; '
                    'border: 1px solid #555; '
                    f'background-color: {hex_color};"></div>')

        return ('<div style="vertical-align: middle;">'
                f'<strong>{self.name}</strong> '
                '</div>'
                '<div class="cmap"><img '
                f'alt="{self.name} colormap" '
                f'title="{self.name}" '
                'style="border: 1px solid #555;" '
                f'src="data:image/png;base64,{png_base64}"></div>'
                '<div style="vertical-align: middle; '
                f'max-width: {_REPR_PNG_SIZE[0]+2}px; '
                'display: flex; justify-content: space-between;">'
                '<div style="float: left;">'
                f'{color_block(self.get_under())} under'
                '</div>'
                '<div style="margin: 0 auto; display: inline-block;">'
                f'bad {color_block(self.get_bad())}'
                '</div>'
                '<div style="float: right;">'
                f'over {color_block(self.get_over())}'
                '</div>')

    def copy(self):
        """Return a copy of the colormap."""
        return self.__copy__()
