%global debug_package %{nil}
%global cdfver 38_0

Name:		libcdf
Version:	3.8.0
Release:	1
Summary:	The NASA Common Data Format implementation
Group:		Development/Libraries
License:	CDF
URL:		http://cdf.gsfc.nasa.gov/
Source0:	ftp://cdaweb.gsfc.nasa.gov/pub/cdf/dist/latest-release/linux/cdf%{cdfver}-dist-all.tar.gz
Source1:	cdf-init-bourne.sh
Source2:	cdf-init-cshell.sh
Source3:	cdf-init-bash.sh
BuildRequires:	gcc-gfortran
BuildRequires:	ed
BuildRequires:	ncurses-devel

%description
The Common Data Format (CDF) is a self-describing data format for the storage
and manipulation of scalar and multidimensional data in a platform- and
discipline-independent fashion. When one first hears the term "Common Data
Format" one intuitively thinks of data formats in the traditional (i.e.
messy/convoluted storage of data on disk or tape) sense of the word. Although
CDF has its own internal self describing format, it consists of more than just
a data format. CDF is a scientific data management package (known as the "CDF
Library") which allows programmers and application developers to manage and
manipulate scalar, vector, and multi-dimensional data arrays. The irony of the
term "FORMAT" is that the actual data format which CDF utilizes is completely
transparent to the user and accessible through a consistent set of interface
(known as the "CDF Interface") routines. Therefore, programmers are not 
burdened with performing low level I/O's to physically format and unformat the
data file. This is all done for them automatically. 

Initialize enviroment variables by running cdf-init-bourne.sh, 
cdf-init-cshell.sh or cdf-init-bash.sh before running.

%package devel
Summary:	CDF development headers
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development headers for cdf.

%prep
%setup -q -n cdf%{cdfver}-dist
#sed -i -e '394s|printf (|printf ("%%s", |' -e '407s|printf (|printf ("%%s", |' src/tools/cdfmerge.c

%build
#make OS=linux ENV=gnu SHARED=yes SHAREDEXT=so CURSES=yes FORTRAN=yes CC_linux_gnu="gcc %{optflags}" FC_linux="gfortran %{optflags}" UCOPTIONS=-Dsingle_underscore all #%{?_smp_mflags} all
make OS=linux ENV=gnu all

%install
rm -rf %{buildroot}
#make install DESTDIR=$RPM_BUILD_ROOT
make INSTALLDIR=%{buildroot}/%{_datadir}/%{name} install

## Move around files
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_libdir} %{buildroot}/%{_includedir}

mv %{buildroot}/%{_datadir}/%{name}/include/* %{buildroot}/%{_includedir}
mv %{buildroot}/%{_datadir}/%{name}/bin/* %{buildroot}/%{_bindir}

# Move dynamic library to libdir and remove static one
mv %{buildroot}/%{_datadir}/%{name}/lib/*.so %{buildroot}/%{_libdir}
rm  %{buildroot}/%{_datadir}/%{name}/lib/*.a

# Help dir
mv %{buildroot}/%{_datadir}/%{name}/lib/cdf/help %{buildroot}/%{_datadir}/%{name}/help

# Remove empty dirs
rmdir %{buildroot}/%{_datadir}/%{name}/lib/cdf %{buildroot}/%{_datadir}/%{name}/lib %{buildroot}/%{_datadir}/%{name}/bin %{buildroot}/%{_datadir}/%{name}/include

# Remove old definition files and install new init ones
rm %{buildroot}/%{_bindir}/definitions.*
sed "s|@BASEDIR@|%{_datadir}/%{name}-%{version}|g;s|@BINDIR@|%{_bindir}|g;s|@LIBDIR@|%{_libdir}|g;s|@INCDIR@|%{_includedir}|g;s|@HELPDIR|%{_datadir}/%{name}-%{version}/help|g" %{SOURCE1} > %{buildroot}/%{_bindir}/cdf-init-bourne.sh
sed "s|@BASEDIR@|%{_datadir}/%{name}-%{version}|g;s|@BINDIR@|%{_bindir}|g;s|@LIBDIR@|%{_libdir}|g;s|@INCDIR@|%{_includedir}|g;s|@HELPDIR|%{_datadir}/%{name}-%{version}/help|g" %{SOURCE2} > %{buildroot}/%{_bindir}/cdf-init-cshell.sh
sed "s|@BASEDIR@|%{_datadir}/%{name}-%{version}|g;s|@BINDIR@|%{_bindir}|g;s|@LIBDIR@|%{_libdir}|g;s|@INCDIR@|%{_includedir}|g;s|@HELPDIR|%{_datadir}/%{name}-%{version}/help|g" %{SOURCE3} > %{buildroot}/%{_bindir}/cdf-init-bash.sh
chmod a+rx %{buildroot}/%{_bindir}/cdf-init*.sh

%clean
rm -rf %{buildroot}

%files
%doc CDF_copyright.txt CHANGES.txt Release.notes samples
%{_bindir}/*
%{_libdir}/libcdf.*.so
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/libcdf.so

%changelog
* Wed Aug 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.0
- Rebuild for Fedora
* Tue Apr 07 2009 Jussi Lehtola <jussi.lehtola@iki.fi> - 3.2.4-1
- First release
