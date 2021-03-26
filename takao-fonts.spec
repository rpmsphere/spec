Name:           takao-fonts
License:        Other uncritical OpenSource License
Group:          System/X11/Fonts
Summary:        "Proportional Gothic" Japanese TrueType font based on IPA fonts
URL:		    https://launchpad.net/takao-fonts
Version:        00303.01
Release:        4.1
Source0:        https://launchpadlibrarian.net/199515720/TakaoFonts_%{version}.tar.xz
BuildArch:      noarch

%description
"Proportional Gothic" Japanese TrueType font based on IPA fonts provided by IPA
(Information-technology Promotion Agency) and maintained by Takao Fonts Maintainers.

%prep
%setup -q -n TakaoFonts_%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/takao
install -m 644 *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/takao

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt README* ChangeLog
%{_datadir}/fonts/takao

%changelog
* Mon May 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 00303.01
- Rebuild for Fedora
* Fri Apr 16 2010 - Satoru Matsumoto <HeliosReds@opensuse.org>
- Update for Takao Fonts version 003.02.01 and
- Takao Ex Fonts version 001.01.01
* Fri Feb 26 2010 - Satoru Matsumoto <HeliosReds@opensuse.org>  
- renamed extension of the fonts from .otf to .ttf.
- added README.SUSE* files.
