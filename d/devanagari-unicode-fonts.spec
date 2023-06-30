%define	fontdir	%{_datadir}/fonts/devanagari-unicode

Name:           devanagari-unicode-fonts
Version:        1
Release:        2.1
Summary:        Twin Devanagari fonts
License:        GPL
Group:          System/X11/Fonts
URL:            https://bombay.indology.info/software/fonts/devanagari/
Source0:        %{name}.zip
BuildArch:      noarch

%description
Nakula and Sahadeva are “twin” Devanagari fonts, which have been developed by
IMRC, India, for the University of Cambridge.

Both fonts are TrueType/OpenType, and are Unicode compliant. Both contain all
the conjuncts and other ligatures (including Vedic accents) likely to be needed
by Sanskritists. Nakula follows the Bombay style of Devanagari, with rounded
glyphs and little thin/thick variation. Sahadeva is in the Calcutta style,
with more angular glyphs and greater contrast between thin and thick strokes.
The actual shapes of some of the glyphs (e.g. initial “a”, retroflex “n”) also
differ according to the style of the font.

%prep
%setup -q -c

%build

%install
install -d %{buildroot}%{fontdir}
install * %{buildroot}%{fontdir}

%files
%{fontdir}/*

%changelog
* Tue May 24 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
