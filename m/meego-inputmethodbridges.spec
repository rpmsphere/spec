%{!?gtk2_binary_version: %define gtk2_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-2.0)}
##%{!?gtk3_binary_version: %define gtk3_binary_version %(pkg-config  --variable=gtk_binary_version gtk+-3.0)}

Name:		meego-inputmethodbridges
Version:	0.2.3
Release:	19.2
Summary:	Meego im module for gtk
Group:		System Environment/Libraries
License:	LGPLv2.1
URL:		http://www.meego.com
Source0:	%{name}-%{version}.tar.bz2
Patch0:		meego-inputmethodbridges-0.2.3-gtk3.patch
Patch1:		meego-inputmethodbridges-0.2.3-gtk2and3.patch
Patch2:		meego-inputmethodbridges-0.2.3-crash.patch

BuildRequires:  pkgconfig(glib-2.0)
##BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(QtCore) >= 4.6.0
BuildRequires:  pkgconfig(QtGui)
BuildRequires:	gcc-c++

##Requires(post): gtk3
Requires(post): gtk2

%description
This package contains Meego im module for gtk.

%prep
%setup -q

%patch0 -p1 -b .gtk3
%patch1 -p1 -b .gtk2and3
%patch2 -p1 -b .crash

%build
libtoolize --automake
autoreconf -v -i
%configure --with-gtk=2.0
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
##rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/*.la
##rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/*.a

%clean
rm -rf %{buildroot}

%post
##%{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache || :
%{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} > /dev/null || :

%postun
##%{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache || :
%{_bindir}/gtk-query-immodules-2.0-%{__isa_bits} > /dev/null || :

%files
%defattr(-,root,root,-)
##%{_libdir}/gtk-3.0/%{gtk3_binary_version}/immodules/*.so
%{_libdir}/gtk-2.0/%{gtk2_binary_version}/immodules/*.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Dec 06 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuild for OSSII
