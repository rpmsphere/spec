%undefine _debugsource_packages

Name:         lzlib
Summary:      LZMA Compression Library
URL:          https://www.nongnu.org/lzip/lzlib.html
Group:        Compression
License:      GPL
Version:      1.13
Release:      1
Source0:      https://download.savannah.gnu.org/releases/lzip/lzlib/lzlib-%{version}.tar.gz

%description
Lzlib is a lossless file compression library based on the LZMA
(Lempel-Ziv-Markov chain-Algorithm) algorithm, designed by Igor
Pavlov. The high compression of LZMA comes from combining two basic,
well-proven compression ideas: sliding dictionaries (i.e. LZ77/78),
and Markov models (i.e. the thing used by every compression
algorithm that uses a range encoder or similar order-0 entropy coder
as its last stage) with segregation of contexts according to what
the bits are used for. Lzlib has an application programming interface
similar to the one of zlib(3).

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --infodir=%{_infodir} \
    --mandir=%{_mandir} \
    --libdir=%{_libdir} \
    --enable-shared
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_infodir}/%{name}.*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.13
- Rebuilt for Fedora
