Name: C
Summary: A pseudo interpreter of the C programming language
Version: 0.05
Release: 2.1
Group: Applications/System
License: GPL
URL: http://labs.cybozu.co.jp/blog/kazuhoatwork/my_projects/c/
Source0: http://labs.cybozu.co.jp/blog/kazuho/archives/c/%{name}-%{version}.tar.gz

%description
In order to write one-liners in C, I created a tiny wrapper for GCC. Without
the need of manual compilation, developers can rapidly create scripts or write
one-liners using the C programming language that runs at native-code speed.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/C
%{_datadir}/man/man1/C.1.*

%changelog
* Sun Nov 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.05
- Rebuild for Fedora
