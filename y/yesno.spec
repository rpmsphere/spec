%undefine _debugsource_packages

Name: yesno
Summary: Simple console program for asking yes/no questions
Version: 0.9.0
Release: 3.1
Group: Utilities
License: GPLv3
URL: https://github.com/kumashiro/yesno
Source0: %{name}-master.zip

%description
yesno is a small program that does one thing: it asks a supplied question and
waits for yes or no answer. User can reply with single stroke (without the
need to confirm with ENTER key) or may be forced to enter full answer. Default
answer can also be given by pressing ENTER without typying anything else.

%prep
%setup -q -n %{name}-master

%build
./autoinit.sh
./configure --prefix=/usr
make %{?_smp_mflags}

%install
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 po/pl/%{name}.mo %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo

%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Thu Mar 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
