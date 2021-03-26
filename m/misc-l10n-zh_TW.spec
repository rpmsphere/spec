%define locale	zh_TW

Name:		misc-l10n-%{locale}
Version:	5
Release:	1.ossii
Summary:	A Collection of l10n-%{locale} add-on files
Summary(zh_TW):	繁體中文化補充檔案收集包
License:	GPL
Group:		User Interface/Desktops
Source0:	%{name}-%{version}.tar.gz
URL:		http://opendesktop.org.tw/
BuildArch:	noarch
Vendor:		Opendesktop.org.tw
Packager:	OSS Integral Institute, Co. Ltd.
#Requires:	
#BuildRequires: 


%description
Traditional chinese l10n add-on files
mainly for the distribution Fedora Core
or the demo platform Pupa.

%description -l %{locale}
主要應用於發行版本 Fedora Core 或是
展示參考平臺 Pupa 的繁體中文本地化檔案補充包。


%prep
%setup -q

%build
for i in *.catin *.po ; do
  case $i in
    *.catin ) gencat -o ${i%%-*}.cat $i ;;
    *.po ) msgfmt -o ${i%%-*}.mo $i ;;
  esac
  rm -f $i
done

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}/install
%__mkdir_p %{buildroot}%{_datadir}/%{name}/uninstall
%__cp * %{buildroot}%{_datadir}/%{name}/install

%post
cd %{_datadir}/%{name}/install
for i in *.desktop *.theme *.server joerc Edutainment.directory flag.png ; do
  case $i in
    *.desktop ) j="%{_datadir}/applications/$i" ;;
    *.theme ) j="%{_datadir}/themes/${i%%.theme}/index.theme" ;;
    *.server ) j="%{_libdir}/bonobo/servers/$i" ;;
    joerc ) j="%{_sysconfdir}/joe/$i" ;;
    Edutainment.directory ) j="%{_datadir}/desktop-directories/$i" ;;
    flag.png ) j="%{_datadir}/locale/l10n/tw/$i" ;;
  esac
  if [ -f $j ] ; then
    cp -f $j ../uninstall/$i
    cp -f $i $j
  fi
done
for i in *.cat *.mo ; do
  case $i in
    *.cat ) j="%{_datadir}/locale/zh/${i%%.cat}" ;;
    *.mo ) j="%{_datadir}/locale/%{locale}/LC_MESSAGES/$i" ;;
  esac
  if [ -f $j ] ; then
    cp -f $j ../uninstall/$i
  else
    touch ../uninstall/$i
  fi
  cp -f $i $j
done


%preun
cd %{_datadir}/%{name}/uninstall
for i in * ; do
  case $i in
    *.desktop ) j="%{_datadir}/applications/$i" ;;
    *.theme ) j="%{_datadir}/themes/${i%%.theme}/index.theme" ;;
    *.server ) j="%{_libdir}/bonobo/servers/$i" ;;
    *.cat ) j="%{_datadir}/locale/zh/${i%%.cat}" ;;
    *.mo ) j="%{_datadir}/locale/%{locale}/LC_MESSAGES/$i" ;;
    joerc ) j="%{_sysconfdir}/joe/$i" ;;
    Edutainment.directory ) j="%{_datadir}/desktop-directories/$i" ;;
    flag.png ) j="%{_datadir}/locale/l10n/tw/$i" ;;
  esac
  if [ -f $j ] ; then
    if [ -s $i ] ; then
      mv -f $i $j
    else
      rm -f $i $j
    fi
  else
    rm -f $i
  fi
done

%clean
%__rm -rf %{buildroot}


%files
%defattr(0644,root,root,0755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*


%changelog
* Fri May 19 2006 Wei-Lun Chao <bluebat@member.fsf.org> 5-1.ossii
- Initial package.
