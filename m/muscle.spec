%undefine _debugsource_packages

Name:           muscle
Version:        3.8.31
Release:        6.1
License:        Public Domain
Group:          Productivity/Scientific/Other
URL:            http://www.drive5.com/muscle
Source:         http://www.drive5.com/%{name}/downloads%{version}/%{name}%{version}_src.tar.gz
BuildRequires:  gcc-c++
Source1:        %{name}-Makefile
Summary:        Multiple sequence alignment

%description
MUSCLE is a program for creating multiple alignments of amino acid or nucleotide
sequences. A range of options is provided that give you the choice of optimizing
accuracy, speed, or some compromise between the two.

%prep
%setup -q -n %{name}%{version}
%__cp %{SOURCE1} src/Makefile
%ifarch aarch64
sed -i 's|-msse2 -mfpmath=sse||' src/Makefile
%endif

%build
cd src
%__make %{_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT/%{_bindir}
%__cp src/muscle $RPM_BUILD_ROOT%{_bindir}/

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc src/README.txt
%{_bindir}/muscle

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.31
- Rebuilt for Fedora
* Sat Jul 24 2010 dom@vbi.vt.edu
- Initial RPM & custom Makefile
