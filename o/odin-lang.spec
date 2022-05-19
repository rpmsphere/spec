Summary: Odin Programming Language
Name: odin-lang
Version: 0.2022.05
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
sed -i 's|^GIT_SHA=.*|GIT_SHA=|' build_odin.sh
rm `find . -name *.dll` `find . -name *.lib`

%build
make

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/Odin
cp -a odin core vendor %{buildroot}%{_libexecdir}/Odin
ln -s ../libexec/Odin/odin %{buildroot}%{_bindir}/odin-lang

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/odin-lang
%{_libexecdir}/Odin

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2022.05
- Rebuilt for Fedora
