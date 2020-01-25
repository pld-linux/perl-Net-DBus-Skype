#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%define		pdir	Net
%define		pnam	DBus-Skype
Summary:	Net::DBus::Skype - Perl access to DBus Skype API
Summary(pl.UTF-8):	Net::DBus::Skype - dostęp z poziomu Perla do API DBus Skype'a
Name:		perl-Net-DBus-Skype
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0b4555c4d04e8f1d271d2bbd2753d14c
URL:		http://search.cpan.org/dist/Net-DBus-Skype/
BuildRequires:	perl-Moose
BuildRequires:	perl-Net-DBus
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module supplies a Perl API into Skype via DBus.

%description -l pl.UTF-8
Ten moduł udostępnia perlowe API do Skype'a poprzez DBus.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo y | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/skype-*
%{perl_vendorlib}/Net/DBus/Skype.pm
%{_mandir}/man1/skype-*.1*
%{_mandir}/man3/Net::DBus::Skype.3pm*
