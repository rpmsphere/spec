%define	fontdir	%{_datadir}/fonts/freehkkai

Summary: Free HK Kai Font
Name: freehkkai-fonts
Version: 1.01
Release: 1
License: CC BY 4.0 International
Group: User Interface/X
URL: https://freehkfonts.opensource.hk/
BuildArch: noarch
Source0: freehkkai-%{version}.zip
Requires: fontconfig

%description
Free Hong Kong Kai-Ti TrueType Font.

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
%doc README.md LICENSE *.txt
%{fontdir}/*.ttf

%changelog
* Wed Dec 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Initial package
