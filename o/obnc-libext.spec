%define debug_package %{nil}

Name: obnc-libext
Summary: Extend Library for OBNC
Version: 0.7.0
Release: 1
Group: Development/Language
License: MPL
URL: https://miasap.se/obnc/
Source0: https://miasap.se/obnc/downloads/%{name}_%{version}.tar.gz
BuildRequires: obnc
BuildRequires: gc-devel
Requires: obnc

%description
The package obnc-libext extends the basic library with modules for
accessing command line arguments and environment variables, printing to
the standard error stream and converting numbers to strings and vice versa,
and for customizing the trap handler.

%prep
%setup -q

%build
./build

%install
./install --prefix=/usr --libdir=%{_lib} --destdir=%{buildroot}
mv %{buildroot}%{_docdir}/obnc/obncdoc/index.html %{buildroot}%{_docdir}/obnc/obncdoc/index-ext.html

%files
%{_includedir}/obnc/ext
%{_libdir}/obnc/ext
%{_docdir}/obnc/obncdoc/index-ext.html
%{_docdir}/obnc/obncdoc/ext

%changelog
* Tue Aug 25 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.0
- Rebuild for Fedora
