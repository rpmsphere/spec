%define	fontdir	%{_datadir}/fonts/freehk

Summary: Free HK Font
Name: freehk-fonts
Version: 1.02
Release: 1
License: CC BY 4.0 International
Group: User Interface/X
URL: https://freehkfonts.opensource.hk/
BuildArch: noarch
Source0: freehkfonts-%{version}.zip
Requires: fontconfig

%description
Free Hong Kong Kai-Shu TrueType Font.

%prep
%setup -q -c

%build

%install
install -d $RPM_BUILD_ROOT%{fontdir}
install -m644 *.ttf $RPM_BUILD_ROOT%{fontdir}/Free-HK-Kai.ttf

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%doc *.md *.txt
%{fontdir}/*.ttf

%changelog
* Mon Feb 06 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.02
- Initial package
