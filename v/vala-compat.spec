%global api_ver 0.18
%global priority 10

Name:           vala-compat
Version:        0.18.1
Release:        11
Summary:        A modern programming language for GNOME

# Most files are LGPLv2.1+, curses.vapi is 2-clause BSD
License:        LGPLv2+ and BSD
URL:            https://live.gnome.org/Vala
#VCS:           git:git://git.gnome.org/vala
# note: do not use a macro for directory name
# as it breaks Colin Walters' automatic build script
# see https://bugzilla.redhat.com/show_bug.cgi?id=609292
Source0:        https://download.gnome.org/sources/vala/0.18/vala-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  glib2-devel
BuildRequires:  libxslt
# only if Vala source files are patched
# BuildRequires:  vala

# for tests
# BuildRequires:  dbus-x11

# alternatives
%global vala_binaries vala valac
%global vala_manpages valac
%global vala_tools_binaries vala-gen-introspect vapicheck vapigen
%global vala_tools_manpages vala-gen-introspect vapigen
Requires(posttrans):   %{_sbindir}/alternatives
Requires(preun):       %{_sbindir}/alternatives


%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code. It's also planned to generate GIDL files when gobject-
introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.

This package is provided to support applications that require API level
%{api_ver}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files for %{name} (API level
%{api_ver}). This is not necessary for using the %{name} compiler.


%package        tools
Summary:        Tools for creating projects and bindings for %{name}
License:        LGPLv2+
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gnome-common intltool libtool pkgconfig
Requires:       gobject-introspection-devel

%description    tools
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains tools to generate Vala projects, as well as API
bindings from existing C libraries, allowing access from Vala programs.


%package        doc
Summary:        Documentation for %{name}
License:        LGPLv2+

BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       devhelp

%description    doc
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains documentation in a devhelp HTML book.


%prep
%setup -q -n vala-%{version}


%build
%configure
# Don't use rpath!
sed -i 's|/lib /usr/lib|/lib /usr/lib /lib64 /usr/lib64|' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
# remove symlinks, using alternatives
for f in %{vala_binaries} %{vala_tools_binaries};
do
    rm $RPM_BUILD_ROOT%{_bindir}/$f
    touch $RPM_BUILD_ROOT%{_bindir}/$f
done
for f in %{vala_manpages} %{vala_tools_manpages};
do
    rm $RPM_BUILD_ROOT%{_mandir}/man1/$f.1*
    touch $RPM_BUILD_ROOT%{_mandir}/man1/$f.1.gz
done
# own this directory for third-party *.vapi files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vala/vapi
rm $RPM_BUILD_ROOT%{_libdir}/libvala-%{api_ver}.la


%check
# make check


%posttrans
/sbin/ldconfig
for f in %{vala_binaries};
do
    %{_sbindir}/alternatives --install %{_bindir}/$f \
      $f %{_bindir}/$f-%{api_ver} %{priority}
done
for f in %{vala_manpages};
do
    %{_sbindir}/alternatives --install %{_mandir}/man1/$f.1.gz \
      $f.1.gz %{_mandir}/man1/$f-%{api_ver}.1.gz %{priority}
done

%posttrans tools
for f in %{vala_tools_binaries};
do
    %{_sbindir}/alternatives --install %{_bindir}/$f \
      $f %{_bindir}/$f-%{api_ver} %{priority}
done
for f in %{vala_tools_manpages};
do
    %{_sbindir}/alternatives --install %{_mandir}/man1/$f.1.gz \
      $f.1.gz %{_mandir}/man1/$f-%{api_ver}.1.gz %{priority}
done

%preun
/sbin/ldconfig
for f in %{vala_binaries};
do
    %{_sbindir}/alternatives --remove $f \
      %{_bindir}/$f-%{api_ver}
done
for f in %{vala_manpages};
do
    %{_sbindir}/alternatives --remove $f.1.gz \
      %{_mandir}/man1/$f-%{api_ver}.1.gz
done

%preun tools
for f in %{vala_tools_binaries};
do
    %{_sbindir}/alternatives --remove $f \
      %{_bindir}/$f-%{api_ver}
done
for f in %{vala_tools_manpages};
do
    %{_sbindir}/alternatives --remove $f.1.gz \
      %{_mandir}/man1/$f-%{api_ver}.1.gz
done


%files
%doc AUTHORS ChangeLog COPYING MAINTAINERS NEWS README THANKS
%ghost %{_bindir}/vala
%ghost %{_bindir}/valac
%{_bindir}/vala-%{api_ver}
%{_bindir}/valac-%{api_ver}
# owning only the directories, they should be empty
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala-%{api_ver}
%{_libdir}/libvala-%{api_ver}.so.*
%ghost %{_mandir}/man1/valac.1.gz
%{_mandir}/man1/valac-%{api_ver}.1.gz

%files devel
%{_includedir}/vala-%{api_ver}
%{_libdir}/libvala-%{api_ver}.so
%{_libdir}/pkgconfig/libvala-%{api_ver}.pc
# directory owned by filesystem
%{_datadir}/aclocal/vala.m4
%{_datadir}/vala/Makefile.vapigen

%files tools
%ghost %{_bindir}/vala-gen-introspect
%ghost %{_bindir}/vapicheck
%ghost %{_bindir}/vapigen
%{_bindir}/vala-gen-introspect-%{api_ver}
%{_bindir}/vapicheck-%{api_ver}
%{_bindir}/vapigen-%{api_ver}
%{_libdir}/vala-%{api_ver}
%{_datadir}/aclocal/vapigen.m4
%{_datadir}/pkgconfig/vapigen*.pc
%ghost %{_mandir}/man1/vala-gen-introspect.1.gz
%ghost %{_mandir}/man1/vapigen.1.gz
%{_mandir}/man1/vala-gen-introspect-%{api_ver}.1.gz
%{_mandir}/man1/vapigen-%{api_ver}.1.gz

%files doc
%doc %{_datadir}/devhelp/books/vala-%{api_ver}


%changelog
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr  5 2013 Michel Salim <salimma@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1
- Update description
- Ensure tools pull in gobject-introspection-devel, since vapigen
  needs .gir files (from vala-0.19.0-2)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep  4 2012 Michel Salim <salimma@fedoraproject.org> - 0.16.1-1
- Update to 0.16.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 12 2012 Michel Salim <salimma@fedoraproject.org> - 0.16.0-4
- Lower priority of alternatives to 10 (prioritize main vala package)
- Remove upgrade-path workaround inherited from Vala

* Fri May 11 2012 Michel Salim <salimma@fedoraproject.org> - 0.16.0-3
- Remove subpackage-renaming logic; not needed since this is the first
  vala-compat release

* Thu May 10 2012 Michel Salim <salimma@fedoraproject.org> - 0.16.0-2
- Reindent description texts to avoid long lines
- Make alternative scriptlet less noisy (Ralph Bean)

* Sat May  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.16.0-1
- Initial package, based on vala-0.16.0-4
