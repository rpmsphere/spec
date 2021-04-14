Name: aasm
Summary: Advanced assembler base files
Version: 0.9.2
Release: 1
Group: Development/Languages
License: GPLv3+
Source0: http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires: gperf

%description
Aasm is an advanced assembler designed to support several target
architectures. It has been designed to be easily extended and,
should be considered as a good alternative to monolithic assembler
development for each new target CPUs and binary file formats.

Aasm should make assembly programming easier for developer, by
providing a set of advanced features: symbol scopes, expressions engine,
big integer support, numerous and accurate warning messages, filter
modules... Its dynamic modular architecture enables aasm to extend
its set of features with plug-ins.

%prep
%setup -q

%build
%configure
make -k -i
sed -i '640,644s|unsigned int|size_t|' asm-sparc/instr.perf
sed -i '94d' asm-sparc/asm.h
sed -i '40,43s|unsigned int|size_t|' asm-x86/instr.perf
sed -i '120d' asm-x86/asm.h
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-asm-x86.1.*
%{_datadir}/emacs/site-lisp/aasm.el*

%changelog
* Wed Oct 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.2
- Rebuilt for Fedora
