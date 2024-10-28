%undefine _debugsource_packages

Name:           xmacro
Group:          Development/Languages
Version:        0.3pre
Release:        20.1
License:        GPL
URL:            https://xmacro.sourceforge.net/
Summary:        Recording and replaying keyboard and mouse events
Source:         %{name}-pre0.3.tar.bz2
BuildRequires:  gcc-c++ libX11-devel libXtst-devel

%description
The XMacro package contains two simple, C++ programs (xmacrorec and xmacroplay)
for recording and replaying keyboard and mouse events on an X server. This
functionality is achieved through the XTest extension. (BTW it would be better
to use the XTrap extension but it's not widespread in precompiled X servers...)
The programs are heavily based on the xremote utility of Jan Ekholm (chakie at
infa.abo.fi).

%prep
%setup -q -n %name-pre0.3
sed -i 's|#include <stdio.h>|#include <iostream>\n#include <iomanip>\n#include <stdio.h>|' *.cpp 

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp xmacroplay $RPM_BUILD_ROOT/usr/bin
cp xmacrorec $RPM_BUILD_ROOT/usr/bin
cp xmacrorec2 $RPM_BUILD_ROOT/usr/bin

%files
%doc COPYING README README.SUSE
%{_bindir}/xmacro*

%changelog
* Wed Nov 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3pre
- Rebuilt for Fedora                                  
* Sat Dec 27 2008 Dmitry Stropaloff <helions8@gmail.com>
- Initial release
- Various changes in source code
