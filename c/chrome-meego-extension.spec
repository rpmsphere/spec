Name:		chrome-meego-extension
Summary: 	Extension for Chrome Meego integration
Group: 		Productivity/Networking/Web/Utilities
Version: 	0.2.0
License: 	LGPLv2.1
URL: 		http://www.meego.com/
Release:	11.1
Source0:	%{name}-%{version}.tar.bz2
Source1:	chromium-browser-ext.sh
Patch0:		%name-0.1.0-fix-64bit.patch
Patch1:		%name-0.1.0-fix-gcc-warnings.patch
Patch2:		chromium-support.patch
Patch3:		%name-0.1.1-64bit-cflags.patch
Patch4: 	support-chrome-extension-installer.patch
BuildRequires:  python
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  zip
BuildRequires:  openssl
BuildRequires:  python-simplejson
BuildRequires:  sqlite-devel
Requires:       chromium-libs

%description
The extension for Chrome MeeGo integration

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%ifarch x86_64
%patch3 -p1
%endif
#%patch4

%build
pushd plugin
../tools/gyp/gyp --depth=`pwd` -fmake
make %{?_smp_mflags}
mv out/Default/lib.target/libnpMeeGoPlugin.so ../extension/chrome-meego-extension/plugin
popd
pushd extension
python ../tools/crxmake/crxmake.py chrome-meego-extension chrome-meego-extension.pem chrome-meego-extension.crx
popd

%install
mkdir -p %{buildroot}%{_libdir}/chrome-meego-extension/
cp -a extension/chrome-meego-extension.crx %{buildroot}%{_libdir}/chrome-meego-extension/
cp -a extension/external_extensions.json %{buildroot}%{_libdir}/chrome-meego-extension/
mkdir -p %{buildroot}%{_libdir}/chrome-meego-extension/installer
install -m 0755 tools/installer/installer.py %{buildroot}%{_libdir}/chrome-meego-extension/installer/installer.py
mkdir -p %{buildroot}/usr/bin/
cp -a %{SOURCE1} %{buildroot}/usr/bin/
chmod 0755 %{buildroot}/usr/bin/chromium-browser-ext.sh

%clean
rm -rf %{buildroot}

%post
python %{_libdir}/chrome-meego-extension/installer/installer.py install %{_libdir}/chrome-meego-extension/external_extensions.json

%posttrans
python %{_libdir}/chrome-meego-extension/installer/installer.py install %{_libdir}/chrome-meego-extension/external_extensions.json

%preun
python %{_libdir}/chrome-meego-extension/installer/installer.py uninstall %{_libdir}/chrome-meego-extension/external_extensions.json

%files
%defattr(-,root,root,-)
%{_libdir}/chrome-meego-extension
%{_libdir}/chrome-meego-extension/chrome-meego-extension.crx
%{_libdir}/chrome-meego-extension/external_extensions.json
%{_bindir}/chromium-browser-ext.sh

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Mar 16 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Tue Nov 23 2010 prusnak@opensuse.org
- rebased patches to fix build
* Fri Nov  5 2010 awafaa@opensuse.org
- Update to version 0.2.0
* Sat Sep 18 2010 glin@novell.com
- Add chrome-meego-extension-0.1.1-64bit-cflags.patch to fix 64bit
  building
- Amend spec file to fix path error
- Install installer.py explicitly instead of copying everything
  in tools/installer
* Tue Sep  7 2010 awafaa@opensuse.org
- Update to version 0.1.1
* Wed Aug  4 2010 andrea@opensuse.org
- fixed 64bit building
- spec file clean up
* Mon Jun 14 2010 dimstar@opensuse.org
- BuildRequire gcc-c++
* Wed Jun  9 2010 awafaa@opensuse.org
- Initial import for openSUSE version 0.1.0
