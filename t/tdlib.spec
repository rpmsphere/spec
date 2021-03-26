#global debug_package %{nil}

Name:           tdlib
Version:        1.1.1
Release:        1
Summary:        Cross-platform library for building Telegram clients
Group:          Development/Libraries/C and C++
License:        Boost Software License 1.0
URL:            https://github.com/tdlib/td
Source0:        https://github.com/tdlib/td/archive/v1.1.1.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake openssl-devel zlib-devel readline-devel

%description
TDLib (Telegram Database library) is a cross-platform library for building
Telegram clients. It can be easily used from almost any programming language.

%package        devel
Summary:        Development files for tdlib
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
Libraries and header files for TDLib.

%prep
%setup -q

%build
%cmake
make

%install
%make_install

%clean
rm -rf %{buildroot}

%files

%files devel
#{_libdir}/lib*.a
#{_includedir}/dlib/

%changelog
* Wed Feb 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuild for Fedora
