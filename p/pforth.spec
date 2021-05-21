Name:           pforth
Version:        28.20180424
Release:        5.1
License:        Public Domain
Summary:        Portable Forth in 'C'
URL:            http://www.softsynth.com/pforth/
Group:          Development/Languages
Source:         %{name}_v28_20180424.zip

%description
PForth is a public domain, portable ANS Forth based on a kernel written in
ANSI 'C'. This makes it easy to port pForth to multiple platforms. So far,
pForth has run on Macs, PCs, SUNs, Amigas, Linux, BeOS, Nokia Communicator,
SGI Indys, 3DO ARM systems, 3DO PowerPC systems, WebTV systems, Hitachi SH4,
OpenTV prototypes, Compaq Ipaq 3970, Sharp LH79520 ARM processor, Ciena
Systems networking hardware, Beagle Board, and some internal projects at
Lucent. If you build pForth for an embedded system, please let me know and I
will add your machine to the list of machines that pForth has run on.

%prep
%setup -n pforth_v28

%build
cd build/unix
CC=gcc make all

%install
cd build/unix
install -Dm755 pforth_standalone ${RPM_BUILD_ROOT}%{_bindir}/%{name}

%files
%doc *.txt
%{_bindir}/pforth

%changelog
* Tue Oct 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 28.20180424
- Rebuilt for Fedora
* Mon May  5 2014 Takashi Tanigawa (MihailJP) - 27.20101121
- First packaging
