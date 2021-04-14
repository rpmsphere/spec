Name: uemacs
Summary: Full screen editor based on MicroEMACS
Version: 4.0.15
Release: 1
Group: Applications/Editors
License: freeware, non-commercial
URL: https://git.kernel.org/pub/scm/editors/uemacs/uemacs.git
Source0: %{name}-%{version}.tar.gz
BuildRequires: ncurses-devel

%description
uEmacs/PK is an enhanced version of MicroEMACS 3.9e. Enhancements
have been incorporated by Petri H. Kutvonen, University of Helsinki,
Finland. uEmacs is currently maintained by Linus Torvalds.
MicroEMACS was written by Dave G. Conroy and greatly modified by
Daniel M. Lawrence.

%prep
%setup -q
sed -i 's|=/usr|=${DESTDIR}/usr|' Makefile

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}/usr/lib
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/em %{buildroot}%{_bindir}/%{name}

%files
%doc README readme.39e
%{_bindir}/%{name}
/usr/lib/.emacsrc
/usr/lib/emacs.hlp

%changelog
* Fri Dec 13 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.15
- Rebuilt for Fedora
