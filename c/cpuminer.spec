Name:		cpuminer
Version:	2.3.2
Release:	5.1
License:	GPL-2.0
Summary:	Optimized CPU-miner for Bitcoin / Litecoin and others
URL:		https://github.com/pooler/cpuminer
Group:		Productivity/Networking/Other
Source:		https://download.sourceforge.net/project/cpuminer/pooler-%{name}-%{version}.tar.gz
BuildRequires:	libcurl-devel jansson-devel

%description
This is a multi-threaded CPU miner for Litecoin and Bitcoin,
fork of Jeff Garzik's reference cpuminer.

See https://bitcointalk.org/index.php?topic=55038.0 for more details.

%prep
%setup -q
sed -i 's/[^ ]*-arm.\$(OBJEXT)//' Makefile.in

%build
%configure
%__make %{?_smp_mflags}

%install
%__make DESTDIR="%{buildroot}" install

%files
%doc AUTHORS ChangeLog COPYING NEWS README example-cfg.json
%{_bindir}/minerd

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuilt for Fedora
