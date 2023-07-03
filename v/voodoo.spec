Name:		voodoo
Summary:	An implementation of the Voodoo programming language
Version:	1.1.4
Release:	1
License:	GPLv2.1
Group:		Development/Languages
URL:		https://inglorion.net/software/voodoo/
Source0:	https://inglorion.net/download/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	ruby nasm
BuildRequires:  rubygem-rdoc
BuildRequires:  rubypick
Requires:	ruby gcc

%description
The Voodoo programming language is a low-level programming language, abstracting
over the platform's instruction set and calling conventions, but otherwise
leaving the programmer free to do anything at all. The Voodoo compiler is written
in Ruby and generates code for i386-compatible, AMD64, ARM, and MIPS CPUs.

%prep
%setup -q

%build
./configure --prefix /usr
make %{?_smp_mflags}
										
%install
rm -rf %{buildroot}
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}/usr/lib/site_ruby %{buildroot}%{_datadir}/ruby

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}*
%{_datadir}/ruby/%{name}*
%{_datadir}/doc/%{name}
%{_datadir}/man/man1/%{name}*

%changelog
* Tue Oct 15 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.4
- Rebuilt for Fedora
