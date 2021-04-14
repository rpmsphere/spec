Name:           cairo-compmgr
Version:        0.3.4
Release:        23.4
License:        LGPLv3
Summary:        Cairo Composite Manager
URL:            http://cairo-compmgr.tuxfamily.org
Group:          System/GUI/Other
Source0:        http://ftp.frugalware.org/pub/other/people/baste/sources/cairo-compmgr/%{name}-%{version}.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  intltool
BuildRequires:  vala-compat-devel vala-comapt vala-compat-tools
BuildRequires:  pkgconfig(cairo)
BuildRequires:  glade3-libgladeui-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libSM-devel
BuildRequires:  sane-backends-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-1.0)
BuildRequires:  GConf2-devel
BuildRequires:  gtk-doc
BuildRequires:  w3m udisks2
BuildRequires:  mesa-libGL-devel

%description
Cairo Composite Manager is a versatile and extensible composite manager
which use cairo for rendering. Plugins can be used to add some cool
effects to your desktop.

%package devel
License:        LGPLv3
Summary:        Cairo Composite Manager -- Development Files
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
Cairo Composite Manager is a versatile and extensible composite manager
which use cairo for rendering. Plugins can be used to add some cool
effects to your desktop.

%prep
%setup -q -n Cairo-Composite-Manager-master
#sed -i -e 's|vala-1\.0|x11 libvala-0.18|' -e 's|gladeui-1\.0|gladeui-2.0|' configure
sed -i -e 's|bfd_section_size(abfd, section)|bfd_section_size(section)|' \
       -e 's|bfd_get_section_vma(abfd, section)|bfd_section_vma(section)|' \
       -e 's|bfd_get_section_flags(abfd, section)|bfd_section_flags(section)|' src/ccm-debug.c

%build
export LIBS='-lm -lgmodule-2.0'
./autogen.sh --prefix=/usr
#configure --enable-perf-plugin
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete -print
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64
%endif
#sed -i 's|/usr/share/pixmaps/%{name}/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING NEWS
%{_bindir}/cairo-compmgr
%{_bindir}/ccm-schema-key-to-gconf
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/%{name}.desktop
%doc %{_mandir}/man1/%{name}.1.gz
%{_libdir}/libcairo_compmgr.so.0*

%files devel
%{_libdir}/libcairo_compmgr.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
#{_datadir}/gtk-doc/html/*
%{_datadir}/vala/vapi/*
%{_libdir}/glade3/modules/libgladeccm.so
%{_datadir}/glade3/catalogs/cairo-compmgr.xml

%changelog
* Wed Apr 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuilt for Fedora
* Fri Jul  1 2011 vuntz@opensuse.org
- Build glade3 catalog: add pkgconfig(gladeui-1.0) BuildRequires
  and create a glade3-catalog-cairo-compmgr subpackage.
- Build gperf plugin by adding pkgconfig(libgtop-2.0) and
  pkgconfig(libwnck-1.0) BuildRequires and pass
  - -enable-perf-plugin to configure.
- Drop fix_desktop_file.patch and instead change the categories of
  the .desktop file with %%suse_update_desktop_file.
* Fri Jun  3 2011 mchang@novell.com
- Initial package for cairo-compmgr 0.3.0.
