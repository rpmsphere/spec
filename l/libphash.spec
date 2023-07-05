%undefine _debugsource_packages

Name:           libphash
Version:        0.9.5
Release:        25.1
Summary:        Open source perceptual hashing library
Group:          System Environment/Libraries
License:        GPLv3
URL:            https://www.phash.org/
Source0:        https://www.phash.org/releases/pHash-%{version}.tar.gz
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
#BuildRequires:  ffmpeg-devel
#BuildRequires:  libsndfile-devel
#BuildRequires:  libsamplerate-devel
BuildRequires:  gcc-c++ 
BuildRequires:  CImg-devel

%description
pHash is a perceptual hashing library that allows you to find similar
media files without them having to be bit-for-bit identical.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n pHash-%{version}

%build
autoreconf -ifv

./configure --prefix=/usr --disable-static --enable-video-hash=no --enable-audio-hash=no --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/pHash.pc

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.5
- Rebuilt for Fedora
