%define _fontdir meslo-lg

Name:           meslo-lg-fonts
Version:        1.2.1
Release:        4.1
License:        Apache-2.0
Summary:        Meslo LG Font Family
URL:            https://github.com/andreberg/Meslo-Font
Group:          System/X11/Fonts
#Source0:       https://github.com/downloads/andreberg/Meslo-Font/Meslo LG v%{version}.zip
Source0:        Meslo_LG_v%{version}.zip
BuildArch:      noarch

%description
Meslo LG is a customized version of Apple's Menlo-Regular font (which is
a customized Bitstream Vera Sans Mono).

%prep
%setup -qn "Meslo LG v%{version}"
# %%doc doesn't work with spaces. Let's rename the file.
mv -f "About Meslo LG v%{version}.pdf" About_Meslo_LG_v%{version}.pdf

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
for f in *.ttf ; do
    install -Dm 644 "${f}" $RPM_BUILD_ROOT%{_datadir}/fonts/%{_fontdir}/"${f}"
done

%files
%doc About_Meslo_LG_v%{version}.pdf
%{_datadir}/fonts/%{_fontdir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Mon May 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Rebuilt for Fedora
* Tue Jun 14 2011 lazy.kent@opensuse.org
- Build requires xorg-x11-devel to provide font(:lang=*)
* Mon Jun 13 2011 lazy.kent@opensuse.org
- Initial package created - 1.0
