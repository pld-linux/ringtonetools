Summary:	Set of tools for creating ringtones and logos for mobile phones
Summary(pl):	Zestaw narzêdzi do tworzenia dzwonków i logo dla telefonów komórkowych
Name:		ringtonetools
Version:	1.06
Release:	0
License:	Kohnian
Source0:	http://65.108.58.129/%{name}/%{name}-%{version}.tar.gz
Group:		Applications/Sound
Url:		http://nakentone.naken.cc/
BuildRoot:  %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ringtone Tools consists of 6 tools (rtttl2nokia, imelody2nokia,
nokia_icon, bmp2nokia_icon, midi2rtttl, imelody2wav). These programs
help in the creation of ringtones and logos for nokia mobile phones.
For more information check the web page at http://nakentone.naken.cc/.

%prep
%setup -q

%build
%{__make}

%install

rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_bindir}

for i in    rtttl2nokia     \
            imelody2nokia   \
            nokia_icon      \
            bmp2nokia_icon  \
            midi2rtttl      \
            imelody2wav     ;   do
    install $i ${RPM_BUILD_ROOT}%{_bindir}/$i
done

#gzip -n9 samples/* LICENSE README

%clean
make clean


%files
%defattr(644,root,root,755)
%doc LICENSE README samples/*
%attr(755,root,root) %{_bindir}/*
