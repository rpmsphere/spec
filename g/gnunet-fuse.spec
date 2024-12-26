%undefine _debugsource_packages

Name:           gnunet-fuse
Version:        0.23.0
Release:        1
Source0:        http://ftpmirror.gnu.org/gnunet/%{name}-%{version}.tar.gz
License:        GPLv2+
Summary:        GNUnet FUSE interface
Group:          Networking/File transfer
URL:            http://gnunet.org/
BuildRequires:  gnunet-devel
BuildRequires:  fuse-devel
BuildRequires:  libsodium-devel
BuildRequires:  libextractor-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  atlas
Requires:       gnunet

%description
This is the GNUnet FUSE interface. GNUnet is a framework for secure
peer-to-peer networking that does not use any centralized or otherwise
trusted services.

%prep
%setup -q
sed -i 's|pthread_mutexattr_setkind_np|pthread_mutexattr_settype|' src/fuse/mutex.c

%build
./configure --prefix=/usr
make

%install
%makeinstall

%files
%doc README AUTHORS ABOUT-NLS ChangeLog COPYING
%{_bindir}/gnunet-*
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Dec 15 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.23.0
- Rebuilt for Fedora
