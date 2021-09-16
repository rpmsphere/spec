Summary: Odin Programming Language
Name: odin-lang
Version: 0.2021.09
Release: 1
License: BSD-3
Group: Development/Language
URL: https://github.com/odin-lang/Odin
Source0: https://github.com/odin-lang/Odin/archive/refs/heads/master.zip#/Odin-master.zip

%description
Odin is a general-purpose programming language with distinct typing, built for
high performance, modern systems, and built-in data-oriented data types.
The Odin Programming Language, the C alternative for the joy of programming.

%prep
%setup -q -n Odin-master
sed -i 's|11|12|' Makefile

%build
make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/Odin
cp -a odin core shared %{buildroot}%{_libexecdir}/Odin
ln -s ../libexec/Odin/odin %{buildroot}%{_bindir}/Odin

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/Odin
%{_libexecdir}/Odin

%changelog
* Sun Sep 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2021.09
- Rebuilt for Fedora
