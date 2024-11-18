Name:           pypanel
License:        GPL
Group:          System/GUI/Other
Version:        2.4
Release:        1
Summary:        PyPanel is a lightweight panel/taskbar written in Python and C for X11 window managers
URL:            https://pypanel.sourceforge.net/
Source0:        PyPanel-%{version}.tar.gz
Requires:       python2-xlib
BuildRequires:  python2-devel imlib2-devel python2-xlib libXft-devel
Source1:        imlib2-config

%description
PyPanel is a lightweight panel/taskbar written in Python and C for X11 window managers. 
It can be easily customized to match any desktop theme or taste. 
PyPanel works with EWMH compliant WMs (Openbox, PekWM, FVWM, etc.) and is distributed 
under the GNU General Public License v2.

%prep
%setup -q -n PyPanel-%{version}
sed -i 's|/usr/lib/|%{_libdir}/|' setup.py
cp %{SOURCE1} .

%build
export PATH=$PATH:.
python2 setup.py build

%install
python2 setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT

#sed -i 's|/usr/bin/python |/usr/bin/python2 |' %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING README PKG-INFO
%{_bindir}/%{name}
%{python2_sitearch}/PyPanel-*-info
%{python2_sitearch}/ppmodule.so
%{python2_sitelib}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
* Mon Dec 29 2008 Dmitry Stropaloff <helions8@gmail.com>
- initial Fedora release
