%global __os_install_post %{nil}

Name: sawzall
Summary: A compiler and runtime for the Sawzall language
Version: 1.0
Release: 14.1
License: open source
Group: Development/Languages
URL: https://github.com/chen3feng/szl
Source0: sawzall-master.zip
BuildRequires: protobuf-devel
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: libicu-devel

%description
An implementation of Google's Sawzall language for
statistical aggregation of log data.

%prep
%setup -q -n szl-master
#sed -i '16i #include <unistd.h>' src/engine/code.cc src/utilities/random_base.cc
#sed -i -e 's|set<|std::set<|' -e 's|map<|std::map<|' src/protoc_plugin/szl_generator.h
#sed -i -e '805s|return false;|return NULL;|' -e '1079s|return false;|return NULL;|' src/engine/form.cc
sed -i 's|wire_format_lite_inl.h|wire_format_lite.h|' src/engine/protocolbuffers.cc
#sed -i '92d' src/protoc_plugin/topologicalsorter-inl.h
#sed -i '/GOOGLE_/d' src/protoc_plugin/topologicalsorter-inl.h src/protoc_plugin/proto-sorter.cc
sed -i '/mutex_.*;/d' src/protoc_plugin/szl_generator.h src/protoc_plugin/szl_generator.cc

%build
#./autogen.sh
%configure
sed -i 's|-Wall|-Wall -Wno-narrowing -fpermissive|' Makefile src/Makefile
make

%install
%make_install

%files
%doc COPYING *.md
%{_bindir}/*
%{_includedir}/google/szl
%{_libdir}/libszl*

%changelog
* Tue Sep 24 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
