%undefine _missing_build_ids_terminate_build

Name: zimbu
Summary: The Zimbu compiler written in Zimbu
Version: 2013.02.01
Release: 7.1
Group: Development/Languages
URL: http://www.zimbu.org/
Source0: http://zimbu.googlecode.com/files/%{name}_2013_02_01.tgz
License: Apache License
BuildRequires: clang
BuildRequires: llvm-devel

%description
Zimbu is an experimental programming language. It is a very practical,
no-nonsense kind of language. It mixes the good things of many existing
languages and avoids their deficiencies. And then throws in a few brand
new ideas.

%prep
%setup -q -n %{name}_2013_02_01

%build
make bootstrap

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 zimbu zimbu2c pluginproto %{buildroot}%{_bindir}

%files
%doc README LICENSE *.txt
%{_bindir}/*

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2013.02.01
- Rebuild for Fedora
