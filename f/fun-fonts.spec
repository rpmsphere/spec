Name: fun-fonts
Summary: free opentype and truetype fonts
Version: 1.0
Release: 5.1
License: Other
Group: System/X11/Fonts
Source0: https://thelinuxbox.org/downloads/fonts/funfonts.tar.gz
BuildArch: noarch
URL: https://thelinuxbox.org/?page_id=3#fonts

%description
These fonts sport a broad range of licenses (some of which are rather
idiosyncratic) but they are all freely redistributable.

%prep
%setup -q -n funfonts

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/fun
cp *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/fun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/fonts/fun

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Mon Jul 27 2009 admin@eregion.de
- initial package
