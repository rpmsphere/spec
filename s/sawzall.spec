Name: sawzall
Summary: A compiler and runtime for the Sawzall language
Version: 1.0
Release: 14.1
License: open source
Group: Development/Languages
URL: https://github.com/google/szl
Source0: %{name}-master.zip
BuildRequires: protobuf-devel
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: libicu-devel

%description
An implementation of Google's Sawzall language for
statistical aggregation of log data.

%prep
%setup -q -n %{name}-master
sed -i '16i #include <unistd.h>' src/engine/code.cc src/utilities/random_base.cc
sed -i -e 's|set<|std::set<|' -e 's|map<|std::map<|' src/protoc_plugin/szl_generator.h
sed -i -e '805s|return false;|return NULL;|' -e '1079s|return false;|return NULL;|' src/engine/form.cc

%build
./autogen.sh
%configure
sed -i 's|-Wall|-Wall -Wno-narrowing|' Makefile src/Makefile
make

%install
%make_install

%files
%doc COPYING README AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_includedir}/google/szl
%{_libdir}/libszl*

%changelog
* Fri Nov 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
