Name: fort77
Summary: Invokes the f2c Fortran translator transparently
Version: 1.18
Release: 4.1
License: GPL
Group: Development/Languages
Source: ftp://metalab.unc.edu/pub/Linux/devel/lang/fortran/fort77-1.18.tar.gz
BuildRequires: perl, f2c
Requires: perl, f2c
BuildArch: noarch

%description 
The fort77 program invokes the f2c command (a Fortran to C translator)
transparently, so it can be used just like a real Fortran compiler.
Fort77 can be used to compile Fortran, C and assembler code and can
link the code with f2c libraries. If you install fort77, you'll also
need to install the f2c package.

%prep
%setup -q

%build
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon May 28 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.18
- Rebuild for Fedora
* Wed Jul 28 1999 Tim Powers <timp@redhat.com>
- started changelog
- built for 6.1
