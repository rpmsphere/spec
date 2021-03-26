Name:               ccons
Version:            0.1
Release:            1
Summary:            Interactive Console for the C Programming Language
Source:             %{name}-master.zip
URL:                https://github.com/asvitkine/ccons
Group:              Development/Languages
License:            MIT
BuildRequires:      cmake
BuildRequires:      libedit-devel
BuildRequires:      llvm34-devel
BuildRequires:      clang-devel

%description
The goal of ccons is to provide an interactive console for the C programming
language, similar to what irb is for Ruby.

%prep
%setup -q -n %{name}-master
sed -i 's|llvm-config|llvm-config-64-3.4|' CMakeLists.txt

%build
%cmake
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Thu Oct 25 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
