Summary: A cross-platform password manager
Name: gorilla
Version: 1.5.3.7
Release: 6.1
License: GPL
Group: Applications/System
Source: %{name}-%{version}.tar.gz
URL: https://github.com/zdia/gorilla
Requires: tk tcl itcl bwidget tcllib
BuildArch: noarch

%description
The Password Gorilla helps you manage your logins. It stores all your user
names and passwords, along with login information and other notes, in a
securely encrypted file. A single "master password" is used to protect the
file. This way, you only need to remember the single master password, instead
of the many logins that you use.

If you want to log in to a service or Web site, the Password Gorilla copies
your user name and password to the clipboard, so that you can easily paste it
into your Web browser or other application. Because the password does not
appear on the screen, Password Gorilla is safe to use in the presence of others.

The convenience of Password Gorilla allows you to choose different, non-intuitive
passwords for each service. An integrated random password generator can provide
one-time passwords, tunable to various services' policies.

Password Gorilla is a tcl/tk application which can run on Linux and Windows,
and the files written are supposed to be compatible between platforms.
This is important for collaboration in heterogenous environments.

%prep
%setup -q

%build

%install
cd sources
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mv twofish/*.tcl .
rm -r itcl3.4 tcllib twofish
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir $RPM_BUILD_ROOT%{_bindir}
ln -s ../share/%{name}/%{name}.tcl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/gorilla
%{_datadir}/gorilla

%changelog
* Tue Feb 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.3.7
- Rebuild for Fedora
* Tue Feb 19 2008 Thomas Uphill <uphill@ias.edu>
- initial build
