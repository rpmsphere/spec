#global __os_install_post %{nil}
#undefine _debugsource_packages

Summary: An experimental programming language
Name: cmajor
Version: 4.2.0
Release: 1
License: BSD
Group: Development/Languages
Source0: https://github.com/slaakko/cmajorm/releases/download/%{version}/%{name}-%{version}-src.tar.bz2
URL: https://sourceforge.net/projects/cmajor/

%description
Cmajor is an experimental programming language strongly influenced by C++ and C#.
It is semantically closer to C++ than C# and syntactically closer to C# than C++.

%prep
%setup -q -n %{name}-%{version}-src
sed -i '12i #include <memory>' %{name}/soulng/util/Time.cpp

%build
%make_build -C %{name}

%install
%make_install -C %{name}

%files 
%doc README.md
#{_bindir}/*
#{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.2.0
- Rebuilt for Fedora
