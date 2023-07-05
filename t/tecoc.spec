%undefine _debugsource_packages

Name:           tecoc
URL:            https://almy.us/teco.html
Version:        0398
Release:        8.1
Summary:        Text Editor and COrrector
License:        opensource
Group:          Productivity/Editors
Source:         https://almy.us/files/%{name}linux%{version}.tar.gz

%description
TECO, that grand old text editor your father used when he was young, is still
available! It is powerful and compact precursor to EMACS and has a completely
nongraphical user interface. This is based on Pete Siemsen's TECOC
implementation, and comes with a copy of the original DECUS TECO documentation.

%prep
%setup -q -n %{name}%{version}
sed -i -e '/sys_nerr/d' -e 's|sys_errlist\[errno\]|strerror(errno)|' src/zlinux.c

%build
PATH=$PATH:.
make -C src %{?_smp_mflags}

%install
install -Dm755 src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}
install lib/* $RPM_BUILD_ROOT%{_libdir}/%{name}
for f in inspect Make mung teco ; do ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/$f ; done

%files
%doc doc/*
%{_bindir}/*
%{_libdir}/%{name}

%changelog
* Sun Nov 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0398
- Rebuilt for Fedora
