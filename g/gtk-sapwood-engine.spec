Summary:        Sapwood theme engine
Name:           gtk-sapwood-engine
Version:        3.0.0
Release:	1
License:        GPL
Group:          System Environment/Libraries
Source:         sapwood-%{version}.tar.gz
BuildRequires:  gtk2-devel
URL:            ftp://ftp.gnome.org/pub/GNOME/sources/gtk-engines

%description
Derived from the pixbuf engine in gtk2-theme-engines.

%prep
%setup -q -n sapwood
sed -i 's/1\.8/1.11/' autogen.sh
sed -i 's|glib/gerror.h|glib.h|' src/sapwood-pixmap.h

%build
./autogen.sh
%configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# no .la, please
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs rm 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README ChangeLog
%attr (755, root, root) %{_libdir}/gtk-2.0/*/engines/libsapwood.so
%attr (755, root, root) %{_libdir}/sapwood/sapwood-server

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuild for Fedora
