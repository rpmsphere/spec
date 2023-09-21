%undefine _debugsource_packages

Name: objeck
Summary: Object-oriented and functional programming language
Version: 2023.7.5
Release: 1
Group: Development/Language
License: BSD-like
URL: https://github.com/objeck/objeck-lang
#Source0: https://github.com/objeck/objeck-lang/archive/v%{version}.tar.gz#/objeck-lang-%{version}.tar.gz
Source0: objeck-linux-%{version}.tar.gz
BuildRequires: openssl-devel
BuildRequires: libuuid-devel
BuildRequires: unixODBC-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_ttf-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_image-devel
BuildRequires: fcgi-devel

%description
Objeck is an object-oriented computer language with functional features.
The language has ties with Java, Scheme and UML. In this language all
data types, except for higher-order functions, are treated as objects.

%prep
%setup -q -n %{name}-linux-%{version}
sed -i 's|-m64||' `find . -name Makefile.*`
sed -i 's|\.\./lib/|/usr/share/%{name}/|' core/shared/sys.h

%build
cd core/release
%ifarch x86_64 aarch64
./deploy_posix.sh 64
%else
./deploy_posix.sh 32
%endif

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a core/release/deploy/lib/* %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
for i in c d r
do
install -m755 core/release/deploy/bin/ob$i %{buildroot}%{_bindir}/%{name}$i
done
install -d %{buildroot}/etc/profile.d

%files
%doc README.md LICENSE
%{_bindir}/%{name}*
%{_datadir}/%{name}

%changelog
* Sun Sep 17 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2023.7.5
- Rebuilt for Fedora
