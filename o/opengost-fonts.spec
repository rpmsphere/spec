%define _fontdir opengost

Name:           opengost-fonts
Version:        0.3
Release:        1.1
License:        OFL-1.1
Summary:        Open-source Russian GOST Fonts
URL:            https://bitbucket.org/fat_angel/opengostfont/overview
Group:          System/X11/Fonts
Source0:        https://bitbucket.org/fat_angel/opengostfont/downloads/opengostfont-otf-%{version}.tar.xz
Source1:        https://bitbucket.org/fat_angel/opengostfont/downloads/opengostfont-ttf-%{version}.tar.xz
BuildArch:      noarch

%description
Open-source version of the fonts by Russian standard GOST 2.304-81
«Letters for drawings».

%package -n opengost-otf-fonts
Summary:        Open-source Russian GOST Fonts (OpenType Format)
Group:          System/X11/Fonts

%description -n opengost-otf-fonts
Open-source version of the fonts by Russian standard GOST 2.304-81
«Letters for drawings».

This package contains fonts in OpenType format.

%package -n opengost-ttf-fonts
Summary:        Open-source Russian GOST Fonts (TrueType Format)
Group:          System/X11/Fonts

%description -n opengost-ttf-fonts
Open-source version of the fonts by Russian standard GOST 2.304-81
«Letters for drawings».

This package contains fonts in TrueType format.

%prep
%setup -q -c
xz -dc %{SOURCE1} | tar -xf -

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}
install -m 0644 opengostfont-otf-%{version}/*.otf \
    $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}
install -m 0644 opengostfont-ttf-%{version}/*.ttf \
    $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}

%files -n opengost-otf-fonts
%doc opengostfont-otf-%{version}/LICENSE
%dir %{_datadir}/fonts/%{_fontdir}
%{_datadir}/fonts/%{_fontdir}/*.otf

%files -n opengost-ttf-fonts
%doc opengostfont-ttf-%{version}/LICENSE
%{_datadir}/fonts/%{_fontdir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Sun Apr  8 2012 lazy.kent@opensuse.org
- Initial package created - 0.2
