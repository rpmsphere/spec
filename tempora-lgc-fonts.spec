%define _fontdir tempora-lgc

Name:           tempora-lgc-fonts
Version:        0.2.1
Release:        4.1
License:        GPL-2.0+
Summary:        Tempora LGC Unicode Fonts
URL:            http://thessalonica.org.ru/en/fonts.html
Group:          System/X11/Fonts
Source0:        http://www.thessalonica.org.ru/downloads/tempora-lgc.otf.zip
Source1:        http://www.thessalonica.org.ru/downloads/tempora-lgc.ttf.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Tempora LGC Unicode is a font family, designed to provide a free
typeface suitable for word processing in languages which use 3 European
alphabets: Latin, Greek and Cyrillic. It may be especially useful for
philologists (mainly slavists and classicists), since it supports
historical Cyrillic letters available in the Unicode standard (including
letters used in Russian  pre-1918 orthography) as well as all accented
combinations and additional characters needed for fully accented Greek
(both classical and modern). Tempora LGC Unicode is a "smart" font,
intended to demonstrate nicities of the OpenType technologie, applicable
to European scripts.

%package otf
Summary:        Tempora LGC Unicode Fonts (OpenType Format)
Group:          System/X11/Fonts

%description otf
Tempora LGC Unicode is a font family, designed to provide a free
typeface suitable for word processing in languages which use 3 European
alphabets: Latin, Greek and Cyrillic. It may be especially useful for
philologists (mainly slavists and classicists), since it supports
historical Cyrillic letters available in the Unicode standard (including
letters used in Russian  pre-1918 orthography) as well as all accented
combinations and additional characters needed for fully accented Greek
(both classical and modern). Tempora LGC Unicode is a "smart" font,
intended to demonstrate nicities of the OpenType technologie, applicable
to European scripts.

This package contains fonts in OpenType format.

%package ttf
Summary:        Tempora LGC Unicode Fonts (TrueType Format)
Group:          System/X11/Fonts

%description ttf
Tempora LGC Unicode is a font family, designed to provide a free
typeface suitable for word processing in languages which use 3 European
alphabets: Latin, Greek and Cyrillic. It may be especially useful for
philologists (mainly slavists and classicists), since it supports
historical Cyrillic letters available in the Unicode standard (including
letters used in Russian  pre-1918 orthography) as well as all accented
combinations and additional characters needed for fully accented Greek
(both classical and modern). Tempora LGC Unicode is a "smart" font,
intended to demonstrate nicities of the OpenType technologie, applicable
to European scripts.

This package contains fonts in TrueType format.

%prep
%setup -q -c
unzip -oq %{SOURCE1}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}
install -m 0644 *.otf $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}
install -m 0644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}

%files otf
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%{_datadir}/fonts/%{_fontdir}/*.otf

%files ttf
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%{_datadir}/fonts/%{_fontdir}/*.ttf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuild for Fedora
* Fri Aug 26 2011 lazy.kent@opensuse.org
- Initial package created - 0.2.1
