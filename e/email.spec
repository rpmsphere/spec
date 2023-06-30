Name:           email
Version:        3.1.3
Release:        4.1
Summary:        A command line SMTP client
Group:          Applications/Internet
License:        GPLv2+
URL:            https://www.cleancode.org/projects/email
Source0:        https://www.cleancode.org/downloads/email/%{name}-%{version}.tar.gz

%description
Email is a program for the Unix environment that sends messages from the 
command line. It let you send email to remote SMTP servers.  Email makes
it simple to implement in cron jobs. You can pipe data into email and it
will accept it as your message which will bypass opening your editor, and
mail it properly. Also, you can tell email to stay quiet and never display
any output (except for errors) when operating.

Email boasts a lot of other qualities as well.

* Email supports SMTP Authentication.
* Email makes it possible to send to multiple recipients and also 
  CC and BCC multiple recipients.
* You can use an address book that is in an easy to format method.
* You are also able to send attachments using a swift flick on the 
  command line to specifying multiple files.
* Personalized signature file with dynamic options.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
cp AUTHORS ChangeLog COPYING README THANKS TODO %{buildroot}%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/doc/%{name}-%{version}
%{_mandir}/man?/%{name}.*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Tue Dec 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.3
- Rebuilt for Fedora
* Fri Jan 11 2008 Fabian Affolter <fabian@bernewireless.net> - 3.1.2-1
- Initial spec for Fedora
