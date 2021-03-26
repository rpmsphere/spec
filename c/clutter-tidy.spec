Name:           clutter-tidy
Version:        1.0.svn303
Release:        1
Summary:        A reference toolkit based on Clutter 
Group:          Development/Libraries
License:        LGPLv2+
URL:            http://www.clutter-project.org/blog/?p=41
Source:         tidy-1.0.svn303.tar.gz
#svn export http://svn.o-hand.com/repos/tidy/trunk tidy
Patch:		tidy-rename-to-clutter-tidy.diff
BuildRequires:  clutter-devel
Requires:	clutter

%description
Tidy is a simple library containing some useful actors and interfaces
which can be used by applications developers; it aims to be simple
and yet provide some high-level classes that Clutter won’t provide.

%package devel
Summary:        clutter-tidy development environment
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       clutter-devel

%description devel
Header files and libraries for building a extension library for the
clutter-tidy.

%prep
%setup -q -n tidy
%patch -p1
sed -i -e 's|1\.5\*|2.*|' -e 's|-1.10||' autogen.sh
sed -i 's|clutter-0.8|clutter-1.0|' configure*

%build
./autogen.sh --prefix=/usr --disable-debug
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libclutter-tidy-1.0.so.*

%files devel
%{_libdir}/pkgconfig/clutter-tidy-1.0.pc
%{_libdir}/libclutter-tidy-1.0.so
%{_libdir}/*.la
%{_includedir}/clutter-0.8/clutter-tidy

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.svn303
- Rebuild for Fedora
