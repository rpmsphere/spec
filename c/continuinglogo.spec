Name:           continuinglogo
Version:        0.005git
Release:        9.1
Summary:        A Logo interpreter mostly Ucblogo compatible
License:        Open Source
Group:          Development/Languages
Source0:        %{name}-master.zip
URL:            https://github.com/luvisi/continuinglogo
BuildRequires:  wxGTK-devel
BuildRequires:  gc-devel
BuildRequires:  portaudio-devel

%description
A Logo interpreter with dynamic scope, shallow binding, tail call optimization,
Lisp 1.5 style FUNARG's, and first class continuations.

%prep
%setup -q -n %{name}-master

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}
install -m755 clogo %{buildroot}%{_bindir}
install -m644 initialize.txt logoinitialize.txt ucblogolib.txt %{buildroot}%{_datadir}/%{name}

%files
%doc TODO README.md INTERNALS COPYING.*
%{_bindir}/clogo
%{_datadir}/%{name}

%changelog
* Wed Sep 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.005git
- Rebuilt for Fedora
