Name:           twister
Version:        0.9.40
Release:        7.1
Summary:        Peer-to-peer microblogging client
License:        MIT
Group:          Productivity/Networking/Other
URL:            http://twister.net.co
Source0:        twister-core-master.zip
Source1:        twister-html-master.zip
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libdb-cxx-devel
BuildRequires:  openssl-devel
Requires:       tkinter
Patch0:         twister-core-aarch64.patch
Source2:	twister.sh

%description
twister is the fully decentralized P2P microblogging platform 
leveraging from the free software implementations of Bitcoin 
and BitTorrent protocols.

%prep
%setup -q -T -b 1 -n twister-html-master
%setup -q -T -b 0 -n twister-core-master
%patch0 -p1

%build
./autotool.sh
%ifarch aarch64
%configure --disable-sse2
%else
%configure
%endif
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a ../twister-html-master %{buildroot}%{_datadir}/%{name}/html
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/doc/%{name}

%changelog
* Thu Jan 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.40
- Rebuilt for Fedora
* Sat Mar 26 2016 Miguel Freitas
- Build 0.9.28
