Name:           deepin-ui
Summary:        UI toolkit for Linux Deepin
License:        GPL-3.0+
Group:          System/GUI/GNOME
Version:        2.0
Release:        12.1
URL:            http://www.linuxdeepin.com
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-demo.desktop
Source2:        distributor-logo.png
BuildRequires:  cairo-devel
BuildRequires:  gcc-c++
#BuildRequires:  webkitgtk-devel
BuildRequires:  python2-devel
BuildRequires:  pygtk2-devel
BuildRequires:  python2-setuptools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
Requires:       pywebkitgtk
Requires:       deepin-utils
Requires:       deepin-gsettings
BuildArch:      noarch

%description
UI toolkit libs for Linux Deepin,Awesome and Beautiful UI libs with LinuxDeepin.

%package demo
Summary:        UI toolkit for Linux Deepin
Group:          Development/Languages/Python
Requires:      %{name} = %{version}

%description demo
UI toolkit libs demos for Linux Deepin,Awesome and Beautiful UI libs with LinuxDeepin.

%prep
%setup -q 

%build

%install
chmod 644 AUTHORS
chmod 644 COPYING
export CFLAGS="$RPM_OPT_FLAGS" 
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

# deepin-ui files install
mkdir -p %{buildroot}%{_datadir}/pyshared
mv %{buildroot}%{_prefix}/dtk %{buildroot}/%{_datadir}/pyshared
rm -rf %{buildroot}%{_datadir}/pyshared/dtk/locale/*.po
rm -rf %{buildroot}%{_datadir}/pyshared/dtk/locale/deepin-ui.pot
mv %{buildroot}%{_datadir}/pyshared/dtk/locale %{buildroot}/%{_datadir}/locale
mkdir -p %{buildroot}%{python2_sitelib}/dtk
cd %{buildroot}%{python2_sitelib}/dtk
ln -s ../../../../share/pyshared/dtk/theme theme 
cd %{_builddir}/%{buildsubdir}

# deepin-ui-demo files install
mkdir %{buildroot}%{_datadir}/applications
mkdir %{buildroot}%{_datadir}/deepin-ui-demo
mkdir %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
cp %{S:1} %{buildroot}%{_datadir}/applications
cp -R app_theme %{buildroot}%{_datadir}/deepin-ui-demo
cp -R skin %{buildroot}%{_datadir}/deepin-ui-demo
cp -R cover %{buildroot}%{_datadir}/deepin-ui-demo
cp -R demo.py %{buildroot}%{_datadir}/deepin-ui-demo
cp %{S:2} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
cd %{buildroot}%{_bindir}
ln -s ../share/deepin-ui-demo/demo.py %{name}-demo
cd %{_builddir}/%{buildsubdir}

# fix permission for all theme.txt files
chmod 0644 %{buildroot}%{_datadir}/pyshared/dtk/theme/*/theme.txt
chmod 0644 %{buildroot}%{_datadir}/deepin-ui-demo/app_theme/*/theme.txt

%find_lang %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/deepin-ui-demo/demo.py

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/pyshared
%{python2_sitelib}/dtk*

%files demo
%{_bindir}/%{name}-demo
%{_datadir}/%{name}-demo
%{_datadir}/applications/%{name}-demo.desktop
%{_datadir}/icons/hicolor/48x48/apps/distributor-logo.png

%changelog
* Fri Jun 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Wed Oct 10 2012 hillwood@linuxfan.org
- Fix permission for all theme.txt files
* Tue Oct  9 2012 hillwood@linuxfan.org
- Add deepin-ui-demo package , it was lost before.
* Sun Oct  7 2012 douglarek@outlook.com
- Updated to 1.0.3git20120929
  * Fix menu item clicked bug
  * Add delete tab feature in TabBox
  * Add ComboButton
  Also more features and bugs fixed
* Wed Sep 26 2012 hillwood@linuxfan.org
- update to 1.0.2git20120911
- add new Paned widget：new ui and animation
- TreeView is more powerful
- Optimize Icon View memory usage
- and more ....
* Tue Sep  4 2012 cfarrell@suse.com
- license update: GPL-3.0+
  No indication of GPL-3.0 "only" licenses in the package
* Sun Sep  2 2012 hillwood@linuxfan.org
- Initial package 1.0git20120817
