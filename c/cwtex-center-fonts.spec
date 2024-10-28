%define fontdir %{_datadir}/fonts/cwtex

Summary:        cwTeX TrueType center fonts
Name:           cwtex-center-fonts
Version:        1.0
Release:        3.1
License:        General Public License
Group:          User Interface/X
BuildArch:      noarch
Source:         ftp://cle.linux.org.tw/pub/fonts/cwttf/cwttf-v%{version}.tar.gz

%description
Those five TrueType fonts (ming,kai,fs,heib,yen face) are transformed
from cwTeX Traditional Chinese Type 1 fonts, and merge Alexej Kryukov's
CM-LGC font and Koanughi Un's Un-Fonts.

%prep
%setup -q -n cwttf

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{fontdir}
install -m 0644 center/*.ttf $RPM_BUILD_ROOT%{fontdir}

%post
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%postun
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%files
%doc AUTHORS COPYING Changes-*.txt Readme*
%{fontdir}/*.ttf

%changelog
* Tue Mar 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Mon Dec 12 2005 Seventeen <seventeen@linux.org.tw>
- first release
