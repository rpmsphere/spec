%define fontdir %{_datadir}/fonts/oppo

Name: opposans-fonts
Summary: OPPOSans truetype fonts
Version: 1.0
Release: 2
Group: User Interface/X
License: freeware
URL: https://bbs.coloros.com/thread-2272309-1-1.html
Source0: http://static01.coloros.com/www/public/img/topic7/font-opposans.zip
Source1: opposans-fonts-copyright
Source2: 86gs-opposans.conf
BuildArch: noarch

%description
5 TTFs include:
OPPOSans-L.ttf (Light)
OPPOSans-R.ttf (Regular)
OPPOSans-M.ttf (Medium)
OPPOSans-B.ttf (Bold)
OPPOSans-H.ttf (Heavy)

%prep
%setup -q -n Font-OPPOSans
cp %{SOURCE1} copyright

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{fontdir}
install -m0644 *.ttf $RPM_BUILD_ROOT%{fontdir}
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/ghostscript/cidfmap.d/86gs-opposans.conf

%files
%license copyright
%{_sysconfdir}/ghostscript/cidfmap.d/86gs-opposans.conf
%{fontdir}

%changelog
* Mon Dec 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
