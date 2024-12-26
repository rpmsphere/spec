Name:           gnunet-gtk
Version:        0.23.0
Release:        1
Source0:        http://ftpmirror.gnu.org/gnunet/%{name}-%{version}.tar.gz
License:        GPLv2+
Summary:        GNUnet GTK user interface
Group:          Networking/File transfer
URL:            http://gnunet.org/
BuildRequires:  libpng-devel
BuildRequires:  gnunet-devel
BuildRequires:  gtk3-devel
BuildRequires:  unique3-devel
BuildRequires:  qrencode-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libextractor-devel
BuildRequires:  glade-devel
BuildRequires:  glade3-libgladeui-devel
BuildRequires:  sane-backends-devel
BuildRequires:  udisks2 atlas

%description
This is the GNUnet GTK user interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

%files -f %{name}.lang
%doc README AUTHORS ABOUT-NLS ChangeLog COPYING
%{_bindir}/gnunet-*
%{_mandir}/man1/*.1.*
%{_datadir}/%{name}
%{_datadir}/applications/gnunet-*.desktop
%{_datadir}/icons/hicolor/*/*/*
%exclude %{_datadir}/icons/hicolor/icon-theme.cache
%{_libdir}/libgnunetgtk.so.*

%package devel
Summary:        GNUnet GTK development files
Group:          System/Libraries
Requires:       %{name} = %{version}

%description devel
This is the GNUnet GTK user interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

This package contains files required for development only.

%files devel
%doc README AUTHORS ABOUT-NLS ChangeLog COPYING
%{_includedir}/%{name}
%{_libdir}/gnunet/libgnunet*.so
%{_libdir}/libgnunetgtk.so

%prep
%setup -q

%build
%configure --with-gtk-version=3.0.0 --with-gnunet=/usr --with-glade=/usr
make

%install
%makeinstall
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnunet
mv %{buildroot}%{_datadir}/gnunet/* %{buildroot}%{_datadir}/%{name}
sed -i 's|Icon=gnunet-setup|Icon=/usr/share/gnunet-gtk/gnunet_logo.png|' %{buildroot}%{_datadir}/applications/gnunet-setup.desktop
%find_lang %{name}

%changelog
* Sun Dec 15 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.23.0
- Rebuilt for Fedora
* Mon Jan 16 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.1-1
+ Revision: 761829
- new tarball
- new version 0.9.1
* Thu Aug 11 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.0-0.pre2.1
+ Revision: 693964
- imported package gnunet-gtk
* Thu Aug 11 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.9.0-0.pre2.1mdv2011.0
- New version 0.9.0pre2
- Port to 2011
* Thu Apr 03 2008 Anssi Hannula <anssi@zarb.org> 0.7.3-1plf2008.1
- add to PLF
- drop duplicate menu entry
- buildrequires libglade2
* Fri Mar 21 2008 Nicolas Vigier <boklm@mars-attacks.org> 0.7.3-1mdv2008.1
- first version
